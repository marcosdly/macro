import { Section, SectionButton } from "../common/Section";

export const StatusSectionButton = () => (
  <>
    <SectionButton title="Status" component={<StatusSection />} />
  </>
);

export function StatusSection() {
  return (
    <Section>
      <p>status</p>
    </Section>
  );
}
