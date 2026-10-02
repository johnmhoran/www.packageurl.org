import React, {useEffect, useState} from 'react';
import CodeBlock from '@theme/CodeBlock';
import useBaseUrl from '@docusaurus/useBaseUrl';

export default function JsonViewer({src, title}) {
  const url = useBaseUrl(src);
  const [text, setText] = useState('Loading…');

  useEffect(() => {
    fetch(url)
      .then((r) => r.text())
      .then(setText)
      .catch((e) => setText(`Failed to load ${url}: ${e}`));
  }, [url]);

  return (
    <CodeBlock language="json" title={title} showLineNumbers>
      {text}
    </CodeBlock>
  );
}
