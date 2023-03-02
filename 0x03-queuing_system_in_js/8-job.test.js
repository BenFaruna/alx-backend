import kue from 'kue';
import chai from 'chai';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();
const should = chai.should();
const expect = chai.expect;

describe('createPushNotificationsJobs', function() {

  before(function(){
    queue.testMode.enter();
  });

  afterEach(function() {
    queue.testMode.clear();
  })

  after(function() {
    queue.testMode.exit();
  });

  it('display a error message if jobs is not an array', function() {
    expect(function() {
      createPushNotificationsJobs(
        {
          phoneNumber: '247287127',
          message: 'This is a test'
        }, queue)
      }
    ).to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', function() {
    const list = [
      { phoneNumber: '258269730180', message: 'This is a test 1'},
      { phoneNumber: '226927024869', message: 'This is a test 2'}
    ];

    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
  });
});

