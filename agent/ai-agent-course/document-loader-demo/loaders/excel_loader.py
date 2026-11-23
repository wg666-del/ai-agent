from pathlib import Path

from openpyxl import load_workbook

from langchain_core.documents import Document


def load_excel(file_path: str):
    path = Path(file_path)

    workbook = load_workbook(
        filename=path,
        read_only=True,
        data_only=True,
    )

    documents = []

    for sheet in workbook.worksheets:
        rows = list(sheet.iter_rows(values_only=True))

        if not rows:
            continue

        headers = [
            str(value).strip()
            if value is not None
            else f"column_{index}"
            for index, value in enumerate(
                rows[0],
                start=1,
            )
        ]

        for row_index, row in enumerate(
            rows[1:],
            start=2,
        ):
            values = []

            for header, value in zip(headers, row):
                if value is None:
                    continue

                values.append(
                    f"{header}: {value}"
                )

            if not values:
                continue

            content = "\n".join(values)

            document = Document(
                page_content=content,
                metadata={
                    "source": path.name,
                    "sheet": sheet.title,
                    "row": row_index,
                    "document_type": "excel",
                }
            )

            documents.append(document)

    workbook.close()

    print(f"Excel 解析完成，共 {len(documents)} 条记录")

    return documents


if __name__ == "__main__":
    load_excel("data/goods_list.xlsx")