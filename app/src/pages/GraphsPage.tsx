import { useEffect, useState } from "react";
import { useSidebar } from "../context/SidebarProvider";
import "../styles/Pages.css";
import "bootstrap/dist/css/bootstrap.css";

// Define the structure of a Project object
interface Project {
  project_id: number; // Unique identifier for the project
  project_name: string; // Name of the project
  last_timestamp: string; // Last updated timestamp for the project
  number_of_entries: number; // Number of entries associated with the project
}

function GraphsPage() {
  // Access the sidebar state using SidebarProvider hook
  const { isOpened } = useSidebar();

  // Hold projects list from database using useState
  const [projects, setProjects] = useState<Project[]>([]);

  // Fetch data with useEffect hook when the component is mounted
  useEffect(() => {
    // Use Electron context bridge to fetch data with preload.js script
    window.electron
      .fetchData() // Fetch data from database
      .then((data: Project[]) => {
        // Update the projects state with the data
        setProjects(data);
      })
      .catch((error: any) => {
        // Log any errors that occur during the fetch
        console.error("Failed to fetch data:", error);
      });
  }, []); // Empty dependency array ensures this runs only once when the component mounts

  return (
    <div className="page">
      <h1
        className={`page-title ${isOpened ? "" : "page-title--sidebar-closed"}`}
      >
        Graphs Page
      </h1>
      <div className="table-responsive">
        <table className="table table-striped table-bordered mt-3">
          <thead className="thead-dark">
            <tr>
              <th scope="col">Project ID</th>
              <th scope="col">Project Name</th>
              <th scope="col">Last Timestamp</th>
              <th scope="col">Number of Entries</th>
            </tr>
          </thead>
          <tbody>
            {/* Iterate over the projects array and render a table row for each project */}
            {projects.map((project) => (
              <tr key={project.project_id}>
                <td>{project.project_id}</td>
                <td>{project.project_name}</td>
                <td>{project.last_timestamp}</td>
                <td>{project.number_of_entries}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default GraphsPage;
