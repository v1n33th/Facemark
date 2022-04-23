import { ReactElement } from "react";
import ErrorLabel from "../error-label/error-label";
import styles from "./text-input.module.css";
type Props = {
  value: string;
  placeholder?: string;
  onChange: (value: string) => void;
  onEnterKeypress?: () => void;
  errorLabel?: string;
};

function TextInput({
  value,
  onChange,
  placeholder,
  onEnterKeypress,
  errorLabel,
}: Props): ReactElement {
  const onKeyPress = (e: any) => {
    if (e.key === "Enter") {
      onEnterKeypress && onEnterKeypress();
    }
  };
  return (
    <>
      <input
        className={styles["input"]}
        type="text"
        value={value}
        onKeyPress={onKeyPress}
        placeholder={placeholder ?? ""}
        onChange={(e) => onChange(e.target.value)}
      />
      <ErrorLabel error={errorLabel} />
    </>
  );
}

export default TextInput;
