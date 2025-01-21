import { useSidebar } from "../context/SidebarProvider";
import { useFlask } from "../context/FlaskProvider";
import "../styles/Pages.css";
import "bootstrap/dist/css/bootstrap.css";

function GraphsPage() {
  // Access the sidebar state using SidebarProvider hook
  const { isOpened } = useSidebar();

  // Access the projects state using ProjectsProvider hook
  const { projects, loading, error } = useFlask();

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

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
