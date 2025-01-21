import { useSidebar } from "../context/SidebarProvider";
import "../styles/Pages.css";

function AboutPage() {
  const { isOpened } = useSidebar();
  return (
    <div className="page">
      <h1
        className={`page-title ${isOpened ? "" : "page-title--sidebar-closed"}`}
      >
        About Us
      </h1>
      {/* Picture and description about Ethan and Felipe */}
      {/* Link to emails, Instagram, Github, Linkedin, etc ? */}
      {/* Shoutout to Professor Hussain */}
    </div>
  );
}

export default AboutPage;
