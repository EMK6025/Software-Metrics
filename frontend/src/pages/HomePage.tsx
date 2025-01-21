import { useSidebar } from "../context/SidebarProvider";
import "../styles/Pages.css";

function HomePage() {
  const { isOpened } = useSidebar();
  return (
    <div className={`page ${isOpened ? "" : "page--sidebar-closed"}`}>
      <h1
        className={`page-title ${isOpened ? "" : "page-title--sidebar-closed"}`}
      >
        Website Title
      </h1>
      <div className="readme">
        <h2 id="features">About this Site</h2>
        <p>
          This project aims to provide Java developers with a quantitative
          measure of the health and quality of their projects. By analyzing
          various code metrics such as cyclomatic complexity, Halstead metrics,
          class complexity, logical LOC, code churn, clone detection, comment
          ratio, code smells, coupling, cohesion, and adherence to SOLID design
          principles, the program generates a comprehensive report to help
          identify areas for improvement. The tool is designed to assist
          developers in maintaining clean, efficient, and scalable codebases by
          providing real-time insights into project quality and streamlining the
          development process.
        </p>
        <h2 id="features">Features</h2>
        <h3 id="complexity-understanding-">Complexity (Understanding)</h3>
        <ul>
          <li>
            <strong>Cyclomatic Complexity</strong>: Measures the complexity of a
            program by counting the number of linearly independent paths through
            the source code.
          </li>
          <li>
            <strong>Halstead Metric</strong>: Analyzes the software&#39;s
            volume, difficulty, and effort based on operators and operands in
            the code.
          </li>
          <li>
            <strong>Complexity per Method/Class</strong>: Evaluates the
            complexity of individual methods or classes to identify areas that
            might need simplification.
          </li>
        </ul>
        <h3 id="maintainability-ease-of-modification-">
          Maintainability (Ease of Modification)
        </h3>
        <ul>
          <li>
            <strong>Logical LOC (Lines of Code)</strong>: Measures the number of
            lines of code that contribute to the logic of the program, excluding
            comments and blank lines.
          </li>
          <li>
            <strong>Churn</strong>: Tracks changes in the code over time to
            identify unstable or frequently modified areas that may indicate
            poor maintainability.
          </li>
          <li>
            <strong>Code Clone Detection</strong>: Identifies duplicate code
            segments that could lead to maintenance challenges and bugs.
          </li>
          <li>
            <strong>Comment:Code Ratio</strong>: Evaluates the balance between
            comments and code, which can indicate how well-documented and
            understandable the code is.
          </li>
        </ul>
        <h3 id="design-oop-structure-">Design (OOP Structure)</h3>
        <ul>
          <li>
            <strong>SOLID Principles</strong>: Checks the code for adherence to
            the SOLID design principles (Single Responsibility, Open/Closed,
            Liskov Substitution, Interface Segregation, Dependency Inversion).
          </li>
          <li>
            <strong>Coupling (God Methods)</strong>: Measures the degree of
            coupling between classes or methods, aiming to avoid excessive
            dependencies that make code harder to modify.
          </li>
          <li>
            <strong>Cohesion</strong>: Assesses the cohesion within classes and
            methods, ensuring that components are logically related and focused
            on specific tasks.
          </li>
          <li>
            <strong>Code Smell Metrics</strong>: Detects &quot;code
            smells,&quot; or patterns in code that suggest possible problems,
            like large methods, excessive conditionals, or duplicate code.
          </li>
        </ul>
      </div>
    </div>
  );
}

export default HomePage;
