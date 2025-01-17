import { useSidebar } from "../context/SidebarProvider";
import "../styles/Pages.css";

function GraphsPage() {
  const { isOpened } = useSidebar();
  return (
    <div className="page">
      <h1
        className={`page-title ${isOpened ? "" : "page-title--sidebar-closed"}`}
      >
        Graphs Page
      </h1>
    </div>
  );
}

export default GraphsPage;
