import "./Sidebar.css";
import { useState } from "react";
import Hamburger from "hamburger-react";

function Sidebar() {
  const [isOpened, setIsOpened] = useState(false);

  function toggleSidebar(toggled: unknown): void {
    if (toggled) {
      setIsOpened(true); // Open the sidebar
    } else {
      setIsOpened(false); // Close the sidebar
    }
  }

  return (
    <>
      <Hamburger toggled={isOpened} toggle={toggleSidebar} color="#fff" />

      <div className={`content ${isOpened ? "open" : "closed"}`}>
        <ul>
          <li>
            <a id="home">Home</a>
          </li>
          <li>
            <a id="about">Projects</a>
          </li>
          <li>
            <a id="services">Graphs</a>
          </li>
          <li>
            <a id="contact">Contact</a>
          </li>
        </ul>
      </div>
    </>
  );
}

export default Sidebar;
