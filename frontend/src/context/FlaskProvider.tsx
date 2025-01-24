import {
  createContext,
  useState,
  useContext,
  ReactNode,
  useEffect,
} from "react";

// Define struct for projects table
interface Project {
  project_id: number;
  project_name: string;
  last_timestamp: string;
  number_of_entries: number;
}

interface FlaskContextType {
  projects: Project[];
  loading: boolean;
  error: string | null;
}

// Define struct for FlaskProvider prop, boilerplate
interface FlaskProviderProps {
  children: ReactNode;
}

// Initialize undefined context
const FlaskContext = createContext<FlaskContextType | undefined>(undefined);

// Define FlaskProvider component
export function FlaskProvider({ children }: FlaskProviderProps) {
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const response = await fetch("http://localhost:5000/api/projects");
        if (!response.ok) {
          throw new Error("Failed to fetch projects");
        }
        const data: Project[] = await response.json();
        setProjects(data);
        setLoading(false);
      } catch (error: any) {
        setError(error.message);
        setLoading(false);
      }
    };

    fetchProjects();
  }, []);

  // Provide the projects state and updater function to child components
  return (
    <FlaskContext.Provider value={{ projects, loading, error }}>
      {children}
    </FlaskContext.Provider>
  );
}

// Define custom hook to use the projects context
export const useFlask = (): FlaskContextType => {
  // Use useContext hook to get the current value of the projects context
  const context = useContext(FlaskContext);

  // throw an error if the hook is used outside of a FlaskProvider
  if (!context) {
    throw new Error("useFlask must be used within a FlaskProvider");
  }

  // Return the context value
  return context;
};
