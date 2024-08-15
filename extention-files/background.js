// background.js
const serverUrl = 'http://localhost:8080'; // URL of the local server

chrome.tabs.onActivated.addListener(activeInfo => {
  chrome.tabs.get(activeInfo.tabId, tab => {
    sendUrlToServer(tab.url);
  });
});

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status === 'complete') {
    sendUrlToServer(tab.url);
  }
});

function sendUrlToServer(url) {
  fetch(serverUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: new URLSearchParams({ 'url': url })
  }).then(response => response.text())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
}
