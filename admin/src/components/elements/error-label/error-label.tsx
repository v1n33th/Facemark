import styles from "./error-label.module.css";

type Props = {
  error?: string;
};

function ErrorLabel({ error }: Props) {
  if (!error) {
    return null;
  }
  return <div className={styles["error-label"]}>{error}</div>;
}

export default ErrorLabel;
