import "../styles/Sidebar.css";
import { Link } from "react-router-dom";
import Hamburger from "hamburger-react";
import { useSidebar } from "../context/SidebarProvider";

function Sidebar() {
  const { isOpened, setIsOpened } = useSidebar();

  return (
    <div className={`container ${isOpened ? "" : "container--closed"}`}>
      <div className="header">
        <div className="icon">
          <Hamburger toggled={isOpened} toggle={setIsOpened} color="#fff" />
        </div>
        <h2 className={`title ${isOpened ? "" : "title--closed"}`}>Menu</h2>
      </div>

      <div className={`content ${isOpened ? "" : "content--closed"}`}>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/projects">Projects</Link>
          </li>
          <li>
            <Link to="/graphs">Graphs</Link>
          </li>
          <li>
            <Link to="/about">About</Link>
          </li>
        </ul>
      </div>
    </div>
  );
}

export default Sidebar;
