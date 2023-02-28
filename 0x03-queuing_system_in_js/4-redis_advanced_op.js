import redis from 'redis';

const client = redis.createClient();

client.hset(1, 'Portland', 50, redis.print);
client.hset(1, 'Seattle', 80, redis.print);
client.hset(1, 'New York', 20, redis.print);
client.hset(1, 'Bogota', 20, redis.print);
client.hset(1, 'Cali', 40, redis.print);
client.hset(1, 'Paris', 2, redis.print);

client.hgetall(1, (err, data) => {
  console.log(data);
});

