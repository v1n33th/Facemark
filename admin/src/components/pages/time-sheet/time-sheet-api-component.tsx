import LoadingButton from "@mui/lab/LoadingButton";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { differenceInHours } from "date-fns";
import { formatDate } from "../../../services/page-services/time-sheet-page-service/time-sheet-page-service";

function TimeSheetApiComponent({ data, error }: { data?: any[]; error?: any }) {
  if (data) {
    return (
      <TableContainer component={Paper}>
        <Table stickyHeader sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell align="right">Index</TableCell>
              <TableCell align="right">User Name</TableCell>
              <TableCell align="right">Punch In</TableCell>
              <TableCell align="right">Punch Out</TableCell>
              <TableCell align="right">Hours In</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {data.map((row, index) => (
              <TableRow
                key={row.name}
                sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
              >
                <TableCell align="right">{index + 1}</TableCell>
                <TableCell align="right">{row.name}</TableCell>
                <TableCell align="right">
                  {formatDate(new Date(row.punchIn), "yyyy-MM-dd hh:mm aaa")}
                </TableCell>
                <TableCell align="right">
                  {formatDate(new Date(row.punchOut), "yyyy-MM-dd hh:mm aaa")}
                </TableCell>
                <TableCell align="right">
                  {differenceInHours(
                    new Date(row.punchOut),
                    new Date(row.punchIn)
                  ) || "-"}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    );
  }

  if (error) {
    return (
      <div>
        <h1>{error.message}</h1>
      </div>
    );
  }

  return (
    <LoadingButton loading variant="outlined">
      Submit
    </LoadingButton>
  );
}

export default TimeSheetApiComponent;
