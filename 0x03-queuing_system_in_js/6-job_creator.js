import kue from 'kue';

const queue = kue.createQueue();
const data = {
  phoneNumber: '2348015572421',
  message: 'This is the code to verify your account',
};

const job = queue.create('push_notification_code', data);
job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', (result) => {
  console.log('Notification job completed');
})
.on('failed', (err) => {
  console.log('Notification job failed');
});

