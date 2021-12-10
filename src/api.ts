import { GithubData, Langs } from "./types";

export async function searchCodeRepo(
  lang: Langs,
  q: string
): Promise<GithubData[]> {
  const response = await fetch(
    `https://api.github.com/search/code?q=${encodeURIComponent(
      q
    )}+in:file+language:${lang}+repo:microsoft/vscode`
  );
  const data = await response.json();

  return data.items as GithubData[];
}
