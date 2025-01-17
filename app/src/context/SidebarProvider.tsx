import {
  createContext,
  useState,
  useContext,
  ReactNode,
  Dispatch,
  SetStateAction,
} from "react";

interface SidebarContextType {
  isOpened: boolean;
  setIsOpened: Dispatch<SetStateAction<boolean>>;
}

interface SidebarProviderProps {
  children: ReactNode;
}

const SidebarContext = createContext<SidebarContextType | undefined>(undefined);

export function SidebarProvider({ children }: SidebarProviderProps) {
  const [isOpened, setIsOpened] = useState<boolean>(true);

  return (
    <SidebarContext.Provider value={{ isOpened, setIsOpened }}>
      {children}
    </SidebarContext.Provider>
  );
}

export const useSidebar = (): SidebarContextType => {
  const context = useContext(SidebarContext);
  if (!context) {
    throw new Error("useSidebar must be used within a SidebarProvider");
  }
  return context;
};
