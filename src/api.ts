import { GithubData, Langs } from "./types";

export async function searchCodeRepo(
  lang: Langs,
  q: string
): Promise<GithubData[]> {
  var api_backend = process.env.REACT_APP_BACKEND_API;

  const response = await fetch(
    `${api_backend}/v1/search?search=${encodeURIComponent(
      q
    )}&language=${lang}&repository=microsoft/vscode`
  );
  const data = await response.json();

  return data.items as GithubData[];
}
