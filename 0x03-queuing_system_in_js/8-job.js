import kue from 'kue';

const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  for (let data of jobs) {
    let job = queue.create('push_notification_code_3', data)
    job.save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });
    job.on('complete', (result) => {
      console.log(`Notification job ${job.id} completed`);
    })
    .on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    })
    .on('progress', (progress, data) => {
      console.log(`Notification job ${job.id} ${progress}%  complete`);
    });
  }
}

export default createPushNotificationsJobs;

