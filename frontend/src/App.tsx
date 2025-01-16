import "./App.css";
import { useState } from "react";
import Sidebar from "./pages/Sidebar";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import ProjectsPage from "./pages/ProjectsPage";
import GraphsPage from "./pages/GraphsPage";
import ContactsPage from "./pages/ContactsPage";

// <Sidebar isOpened={isOpened} setIsOpened={setIsOpened} />

function App() {
  const [isOpened, setIsOpened] = useState(true);
  return (
    <div className="App">
      <Router>
        <Sidebar isOpened={isOpened} setIsOpened={setIsOpened} />
        <div
          className={`main-content ${
            isOpened ? "sidebar-opened" : "sidebar-closed"
          }`}
        >
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/projects" element={<ProjectsPage />} />
            <Route path="/graphs" element={<GraphsPage />} />
            <Route path="/contacts" element={<ContactsPage />} />
          </Routes>
        </div>
      </Router>
    </div>
  );
}

export default App;
