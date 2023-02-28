import redis from 'redis';

const client = redis.createClient();

client.on('error', err => {
  console.log('Redis client not connected to the server:', err.message);
})
.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.subscribe('holberton school channel');

client.on('message', function(channel, message) {
  if (client.connected) {
    console.log(message);
  }
 
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
    client.end(true);
  }
});

