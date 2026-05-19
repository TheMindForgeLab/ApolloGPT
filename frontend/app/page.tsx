import LeftPanel from "../components/layout/LeftPanel";
import CenterWorkspace from "../components/layout/CenterWorkspace";
import RightInspector from "../components/layout/RightInspector";

export default function Page() {
  return (
    <main className="app-shell">
      <LeftPanel />
      <CenterWorkspace />
      <RightInspector />
    </main>
  );
}
