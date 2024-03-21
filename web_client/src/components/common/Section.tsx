import { Component, VNode, createRef } from "preact";
import { ConfigurationSectionButton } from "../configuration/ConfigurationSection";
import { StatusSectionButton } from "../status/StatusSection";
import { useContext, useEffect } from "preact/hooks";
import { MainContext } from "../../lib/context";
import "./section.scss";

interface SectionButtonProps {
  title: string;
  component: VNode;
}

export class Section extends Component {
  render() {
    return (
      <div id="section">
        <div id="section-content">{this.props.children}</div>
      </div>
    );
  }
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
    <button className="btn btn-primary" onClick={click} ref={ref} type="button">
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
