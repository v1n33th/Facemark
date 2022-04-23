import TextField from "@mui/material/TextField";
import { AdapterDateFns } from "@mui/x-date-pickers/AdapterDateFns";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { DatePicker } from "@mui/x-date-pickers/DatePicker";
import { useState } from "react";
import styles from "./TimeSheet.module.css";
import useSWR from "swr";
import { useSwrFetcher } from "../../../services/api/api-configure";
import { formatDate } from "../../../services/page-services/time-sheet-page-service/time-sheet-page-service";
import { addDays } from "date-fns";
import TimeSheetApiComponent from "./time-sheet-api-component";

export default function TimeSheetPage() {
  const [startDate, setStartDate] = useState<any>(new Date());
  const [endDate, setEndDate] = useState<any>(addDays(new Date(), 1));
  const { data, error } = useSwrFetcher(
    `users/timesheet/${formatDate(startDate)}/${formatDate(endDate)}`
  );
  return (
    <div className={styles["mainDiv"]}>
      <LocalizationProvider dateAdapter={AdapterDateFns}>
        <DatePicker
          label="Start Date"
          value={startDate}
          onChange={(newValue) => {
            setStartDate(newValue);
          }}
          renderInput={(params) => <TextField {...params} />}
        />
        <DatePicker
          label="End Date"
          value={endDate}
          onChange={(newValue) => {
            setEndDate(newValue);
          }}
          renderInput={(params) => <TextField {...params} />}
        />
      </LocalizationProvider>
      <TimeSheetApiComponent data={data} error={error} />
    </div>
  );
}
