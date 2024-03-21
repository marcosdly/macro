import { SectionButton } from "../common/Section";

export const StatusSectionButton = () => (
  <>
    <SectionButton title="Status" component={<StatusSection />} />
  </>
);

export function StatusSection() {
  return (
    <>
      <p>status</p>
    </>
  );
}
