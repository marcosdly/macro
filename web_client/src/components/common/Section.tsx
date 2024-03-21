import { VNode, createRef } from "preact";
import { ConfigurationSectionButton } from "../configuration/ConfigurationSection";
import { StatusSectionButton } from "../status/StatusSection";
import { useContext, useEffect } from "preact/hooks";
import { MainContext } from "../../lib/context";

interface SectionButtonProps {
  title: string;
  component: VNode;
}

export function SectionButton({ title, component }: SectionButtonProps) {
  const [section, setSection] = useContext(MainContext);
  const ref = createRef();

  const click = (event: MouseEvent) => {
    event.preventDefault();
    setSection(component);
  };

  useEffect(() => {
    const elem = ref.current! as HTMLButtonElement;
    if (section.type === component.type) elem.disabled = true;
    else elem.disabled = false;
  }, [section]);

  return (
    <button onClick={click} ref={ref} type="button">
      {title}
    </button>
  );
}

export function SectionAggregator() {
  return (
    <div id="section-aggregator">
      <ConfigurationSectionButton />
      <StatusSectionButton />
    </div>
  );
}
