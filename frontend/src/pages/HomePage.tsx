import { useSidebar } from "../context/SidebarProvider";
import "../styles/Pages.css";

function HomePage() {
  const { isOpened } = useSidebar();
  return (
    <div className="page">
      <h1
        className={`page-title ${isOpened ? "" : "page-title--sidebar-closed"}`}
      >
        Home Page
      </h1>
    </div>
  );
}

export default HomePage;
