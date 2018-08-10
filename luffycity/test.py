import redis

conn = redis.Redis(host='192.168.11.134', port=6379)

# 设置值
conn.set('lvy_name', 'lvy')
# 获取值
var = conn.get('lvy_name').decode('utf8')
print(var)
