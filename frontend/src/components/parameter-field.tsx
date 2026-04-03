import type { FieldName } from "@/lib/types";

interface ParameterFieldProps {
  id: FieldName;
  label: string;
  helper: string;
  placeholder: string;
  value: string;
  error?: string;
  inputMode: "decimal" | "numeric";
  onChange: (field: FieldName, value: string) => void;
}

export function ParameterField({
  id,
  label,
  helper,
  placeholder,
  value,
  error,
  inputMode,
  onChange,
}: ParameterFieldProps) {
  const helperId = `${id}-helper`;
  const errorId = `${id}-error`;

  return (
    <label className="field">
      <span className="field-label-row">
        <span className="field-label">{label}</span>
        <span className="field-helper">{helper}</span>
      </span>
      <input
        id={id}
        name={id}
        type="text"
        inputMode={inputMode}
        value={value}
        placeholder={placeholder}
        autoComplete="off"
        aria-invalid={error ? "true" : "false"}
        aria-describedby={error ? `${helperId} ${errorId}` : helperId}
        className={error ? "field-input field-input-error" : "field-input"}
        onChange={(event) => onChange(id, event.target.value)}
      />
      <span id={helperId} className="field-caption">
        {helper}
      </span>
      {error ? (
        <span id={errorId} className="field-error" role="alert">
          {error}
        </span>
      ) : null}
    </label>
  );
}
