import { GithubData, Langs } from "./types";

export async function searchCodeRepo(
  lang: Langs,
  q: string
): Promise<GithubData[]> {
  const response = await fetch(
    `/api/v1/search?search=${encodeURIComponent(
      q
    )}&language=${lang}&repository=microsoft/vscode`
  );
  const data = await response.json();

  return data.items as GithubData[];
}
