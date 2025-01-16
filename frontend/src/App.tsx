import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { SidebarProvider } from "./context/SidebarProvider";
import Sidebar from "./pages/Sidebar";
import HomePage from "./pages/HomePage";
import ProjectsPage from "./pages/ProjectsPage";
import GraphsPage from "./pages/GraphsPage";
import ContactsPage from "./pages/ContactsPage";

function App() {
  return (
    <div className="App">
      <SidebarProvider>
        <Router>
          <Sidebar />
          <div className="main-content">
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/projects" element={<ProjectsPage />} />
              <Route path="/graphs" element={<GraphsPage />} />
              <Route path="/contacts" element={<ContactsPage />} />
            </Routes>
          </div>
        </Router>
      </SidebarProvider>
    </div>
  );
}

export default App;
