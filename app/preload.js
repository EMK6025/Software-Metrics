const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electron', {
  fetchData: () => ipcRenderer.invoke('fetch-data'),
});