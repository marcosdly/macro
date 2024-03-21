import { SectionButton } from "../common/Section";

export const ConfigurationSectionButton = () => (
  <>
    <SectionButton title="Configuration" component={<ConfigurationSection />} />
  </>
);

export function ConfigurationSection() {
  return (
    <>
      <p>config</p>
    </>
  );
}
