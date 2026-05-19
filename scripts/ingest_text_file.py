from pathlib import Path
import argparse
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from apollo.knowledge.ingestion_pipeline import IngestionPipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest a UTF-8 text/markdown file into ApolloGPT memory.")
    parser.add_argument("path")
    parser.add_argument("--project", default="ApolloGPT")
    parser.add_argument("--memory-type", default="document")
    args = parser.parse_args()

    result = IngestionPipeline().ingest_file(args.path, project=args.project, memory_type=args.memory_type)
    print(f"Ingested {result['source']}")
    print(f"Chunks: {result['chunks']}")


if __name__ == "__main__":
    main()

