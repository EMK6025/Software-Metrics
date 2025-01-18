import {
  createContext,
  useState,
  useContext,
  ReactNode,
  Dispatch,
  SetStateAction,
} from "react";

// Define the structure of the context that will be used in the other React components
interface SidebarContextType {
  isOpened: boolean; // tracks whether the sidebar is open or closed
  setIsOpened: Dispatch<SetStateAction<boolean>>; // Function to toggle the isOpened state
}

// Define the structure of the prop that the SidebarProvider component will accept
interface SidebarProviderProps {
  children: ReactNode; // The children components that the SidebarProvider will wrap
}

// Initialize the undefined context
const SidebarContext = createContext<SidebarContextType | undefined>(undefined);

// Define the SidebarProvider component
export function SidebarProvider({ children }: SidebarProviderProps) {
  // Use useState hook to manage the sidebar's open/close state
  const [isOpened, setIsOpened] = useState<boolean>(true);

  // Provide the sidebar state and updater function to child components
  return (
    <SidebarContext.Provider value={{ isOpened, setIsOpened }}>
      {children}
    </SidebarContext.Provider>
  );
}

// Define custom hook to use the sidebar context
export const useSidebar = (): SidebarContextType => {
  // Use useContext hook to get the current value of the sidebar context
  const context = useContext(SidebarContext);

  // throw an error if the hook is used within a SidebarProvider
  if (!context) {
    throw new Error("useSidebar must be used within a SidebarProvider");
  }

  // Return the context value
  return context;
};
