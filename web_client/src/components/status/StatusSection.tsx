import { Section, SectionButton } from "../common/Section";
import { Start } from "./Start";
import "./status.scss";

export const StatusSectionButton = () => (
  <>
    <SectionButton title="Status" component={<StatusSection />} />
  </>
);

export function StatusSection() {
  return (
    <Section>
      <Start />
    </Section>
  );
}
