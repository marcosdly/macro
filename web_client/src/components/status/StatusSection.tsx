import { Section, SectionButton } from "../common/Section";
import { Feedback } from "./Feedback";
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
      <Feedback />
    </Section>
  );
}
