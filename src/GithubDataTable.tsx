import {
  Table,
  TableContainer,
  TableHead,
  TableRow,
  TableCell,
  Paper,
  TableBody,
  Typography,
  Link,
} from "@mui/material";
import { GithubData } from "./types";

export function GithubDataTable({ data }: { data: GithubData[] }) {
  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Name</TableCell>
            <TableCell>Path</TableCell>
            <TableCell>GitHub Link</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map((row) => (
            <TableRow key={row.url}>
              <TableCell>
                <Typography variant="body1">{row.name}</Typography>
              </TableCell>

              <TableCell>
                <Typography variant="body1">{row.path.slice(0, 20)}</Typography>
              </TableCell>

              <TableCell>
                <Link href={row.html_url} target="_blank">
                  Open on GitHub
                </Link>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
