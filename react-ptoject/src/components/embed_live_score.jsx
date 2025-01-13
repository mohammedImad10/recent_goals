import React, { useEffect } from "react";

const ScorebatEmbed = () => {
  useEffect(() => {
    // Dynamically load the Scorebat script
    const script = document.createElement("script");
    script.src = "https://www.scorebat.com/embed/embed.js?v=arrv";
    script.id = "scorebat-jssdk";
    script.async = true;
    document.body.appendChild(script);

    return () => {
      // Cleanup script when the component unmounts
      document.body.removeChild(script);
    };
  }, []);

  return (
    <div
      style={{
        width: "100%",
        height: "760px",
        overflow: "hidden",
        display: "block",
      }}
    >
      <iframe
        src="https://www.scorebat.com/embed/livescore/?token=MTQzMTkxXzE3MzYxNTc5MzBfZGQ2YjVlZjRkNWJhMGY0MDg3MmU2OTJjNjA2YTcxOGFhZDFkYTA1Mg=="
        frameBorder="0"
        width="600"
        height="760"
        allowFullScreen
        allow="autoplay; fullscreen"
        style={{ width: "100%", height: "760px", overflow: "hidden" }}
        className="_scorebatEmbeddedPlayer_"
      ></iframe>
    </div>
  );
};

export default ScorebatEmbed;
