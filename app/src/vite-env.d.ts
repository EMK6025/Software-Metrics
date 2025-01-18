/// <reference types="vite/client" />

interface Window {
    electron: {
      fetchData: () => Promise<Project[]>;
    };
  }
  