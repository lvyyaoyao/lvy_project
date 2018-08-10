import redis, json

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response

from api import models
from api.utils.response import BaseResponse

CONN = redis.Redis(host='192.168.11.134', port=6379)
USER_ID = 1


class ShoppingCarView(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        ret = BaseResponse()
        # 购物车详细信息
        try:
            shopping_car_course_list = []
        #     pattern = 'shopping_car_%s_*'%(USER_ID)
            pattern = settings.LUFFY_SHOPPING_CAR % (USER_ID, '*')

            user_key_list = CONN.keys(pattern)
            print(user_key_list)
            for key in user_key_list:
                temp = {
                    'id': CONN.hget(key, 'id').decode('utf-8'),
                    'name': CONN.hget(key, 'name').decode('utf-8'),
                    'img': CONN.hget(key, 'img').decode('utf-8'),
                    'default_price_id': CONN.hget(key, 'default_price_id').decode('utf-8'),
                    'price_policy_dict': json.loads(CONN.hget(key, 'price_policy_dict').decode('utf-8')),
                }
                shopping_car_course_list.append(temp)
            ret.data = shopping_car_course_list
        except Exception as e:
            ret.code = 500
            ret.error = '获取购物车失败'
        return Response(ret.dict)

    def create(self, request, *args, **kwargs):
        '''
        1、 接受拥护传过来的课程id和用户id
        2. 判断合法性
            - 课程是否存在？
            - 价格策略是否合法？
        3. 把商品和价格策略信息放入购物车 SHOPPING_CAR

        注意：用户ID=1目前定死
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        # 1、接受拥护传过来的课程id和用户id
        ret = BaseResponse()
        try:
            course_id = request.data.get('courseid')
            policy_id = request.data.get('policyid')

            # 2、判断合法性
            # (1)课程是否存在？
            course = models.Course.objects.filter(id=course_id).first()
            if not course:
                ret.code = 500
                ret.error = '课程不存在！'
                return Response(ret.dict)

            # （2）价格是否合法？
            price_policy_queryset = course.price_policy.all()
            price_policy_dict = {}
            for item in price_policy_queryset:
                temp = {
                    'id': item.id,
                    'price': item.price,
                    'valid_period': item.valid_period,
                    'valid_period_display': item.get_valid_period_display(),
                }
                price_policy_dict[item.id] = temp
            if policy_id not in price_policy_dict:
                ret.code = 502
                ret.error = '价格不存在！'
                return Response(ret.dict)

            # 3、将合法的商品放入购物车
            '''
            其中购物车里面要存在那些内容：
                    1、课程ID
                    2、课程名称
                    3、课程图片
                    4、默认选中价格
                    5、所有价格
                    其储存格式：
                    {
                        shopping_car_1_1（key路径拼接包含用户ID和课程ID）:{
                            id:课程ID
                            name:课程名称
                            img:课程图片
                            defaut:默认选中的价格策略
                            price_list:所有价格策略
                        },
                        shopping_car_1_2:{
                            id:课程ID
                            name:课程名称
                            img:课程图片
                            defaut:默认选中的价格策略
                            price_list:所有价格策略
                        },
                    }

            '''

            # 此段程序为设置购物车空间大小
            pattern = settings.LUFFY_SHOPPING_CAR % (USER_ID, '*')
            keys = CONN.keys(pattern)
            if keys and len(keys) >= 1000:
                ret.code = 505
                ret.error = '购物车东西太多，先去结算再进行购买..'
                return Response(ret.dict)

            key = settings.LUFFY_SHOPPING_CAR % (USER_ID, course_id)
            CONN.hset(key, 'id', course_id)
            CONN.hset(key, 'name', course.name)
            CONN.hset(key, 'img', course.course_img)
            CONN.hset(key, 'default_price_id', policy_id)
            CONN.hset(key, 'price_policy_dict', json.dumps(price_policy_dict))
            ret.code = 200
            ret.error = '购买成功'
            return Response(ret.dict)
        except Exception as e:
            ret.code = 500
            ret.error = '获取购物车失败'
            return Response(ret.dict)

    def destroy(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            courseid = request.GET.get('courseid')
            key = settings.LUFFY_SHOPPING_CAR % (USER_ID, courseid)

            CONN.delete(key)
            ret.data = '删除成功'
        except Exception as e:
            ret.code = 505
            ret.error = '删除失败'
        return Response(ret.dict)

    def update(self, request, *args, **kwargs):
        response = BaseResponse()
        try:
            course_id = request.data.get('courseid')
            policy_id = str(request.data.get('policyid')) if request.data.get('policyid') else None

            key = settings.LUFFY_SHOPPING_CAR % (USER_ID, course_id,)

            if not CONN.exists(key):
                response.code = 500
                response.error = '课程不存在'
                return Response(response.dict)

            price_policy_dict = json.loads(CONN.hget(key, 'price_policy_dict').decode('utf-8'))
            if policy_id not in price_policy_dict:
                response.code = 502
                response.error = '价格策略不存在'
                return Response(response.dict)

            CONN.hset(key, 'default_price_id', policy_id)
            # CONN.expire(key, 20 * 60)   # 定时清除redis中的缓存数据
            response.data = '修改成功'
        except Exception as e:
            response.code = 509
            response.error = '修改失败'
        return Response(response.dict)
