const getHighlights = async (page = 1) => {
  try {
      const response = await fetch(`http://127.0.0.1:8000/batHighlights/highlights/?page=${page}`);

      if (!response.ok) {
          throw new Error("Failed to fetch highlights.");
      }

      const data = await response.json();
      return data;
  } catch (error) {
      console.error("Error fetching highlights:", error);
      throw error;
  }
};

export { getHighlights };
