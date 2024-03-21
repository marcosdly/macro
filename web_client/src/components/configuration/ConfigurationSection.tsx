import { Section, SectionButton } from "../common/Section";
import { SelectVideoInput } from "./SelectVideoInput";
import "./configuration.scss";

export const ConfigurationSectionButton = () => (
  <>
    <SectionButton title="Configuration" component={<ConfigurationSection />} />
  </>
);

export function ConfigurationSection() {
  return (
    <Section>
      <SelectVideoInput />
    </Section>
  );
}
