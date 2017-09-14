const get = url => {
  return new Promise((resolve, reject) => {
    const req = new XMLHttpRequest();
    req.open('GET', url);

    req.onload = () => {
      if (req.status == 200) {
        resolve(req.response);
      } else {
        reject(Error(req.statusText));
      }
    }

    req.onerror = () => {
      reject(Error('Network Error'));
    }

    req.send();
  })
}

get('static/story.json').then(response => {
  console.log('Success!', response);
}, error => {
  console.error('Failed!', response);
})