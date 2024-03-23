import { useState } from "preact/hooks";
import "./app.scss";
import { MainContext } from "./lib/context";
import { SectionAggregator } from "./components/common/Section";
import { ConfigurationSection } from "./components/configuration/ConfigurationSection";
import { VNode } from "preact";
import "./lib/eel";

export function App() {
  // Create section aggregator object first because the button state is based
  // on section state with useEffect
  const aggregator = <SectionAggregator />;
  const [section, setSection] = useState<VNode>(<ConfigurationSection />);

  return (
    <>
      <MainContext.Provider value={[section, setSection]}>
        {aggregator}
        {section}
      </MainContext.Provider>
    </>
  );
}
