import "../styles/Sidebar.css";
import { Link } from "react-router-dom";
import Hamburger from "hamburger-react";

interface SidebarProps {
  isOpened: boolean;
  setIsOpened: React.Dispatch<React.SetStateAction<boolean>>;
}

function Sidebar({ isOpened, setIsOpened }: SidebarProps) {
  return (
    <div className={`container ${isOpened ? "" : "closed"}`}>
      <div className="header">
        <div className="icon">
          <Hamburger toggled={isOpened} toggle={setIsOpened} color="#fff" />
        </div>
        <h2 className={`title ${isOpened ? "" : "closed"}`}>Sidebar Title</h2>
      </div>

      <div className={`content ${isOpened ? "" : "closed"}`}>
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
            <Link to="/contacts">Contact</Link>
          </li>
        </ul>
      </div>
    </div>
  );
}

export default Sidebar;
