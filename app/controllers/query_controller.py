# from app.models.query_model import QueryModel
# import matplotlib.pyplot as plt
# import io
# import base64
# import pandas as pd
# import time
# from typing import Tuple, Dict, Any, Optional

# class QueryController:
#     @staticmethod
#     def generate_visualization(data: Any) -> Tuple[Optional[str], Optional[str]]:
#         """Generate a simple bar or line chart from numerical data.

#         Args:
#             data: Query result data (list, dict, or single value).

#         Returns:
#             Tuple containing base64-encoded image (or None) and error message (or None).
#         """
#         try:
#             # Handle single-value results (e.g., counts)
#             if isinstance(data, (int, float)):
#                 plt.figure(figsize=(4, 4))
#                 plt.bar([0], [data], color='skyblue')
#                 plt.xticks([0], ['Count'])
#                 plt.ylabel('Value')
#                 plt.title('Query Result')
#                 buffer = io.BytesIO()
#                 plt.savefig(buffer, format='png')
#                 buffer.seek(0)
#                 image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
#                 plt.close()
#                 return image_base64, None

#             # Handle list or dict data
#             df = pd.DataFrame(data)
#             numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

#             if len(numerical_cols) == 0:
#                 return None, "No numerical data available for visualization."

#             plt.figure(figsize=(8, 6))
#             if len(df) <= 10:  # Bar plot for small datasets
#                 plt.bar(df.index, df[numerical_cols[0]], color='skyblue')
#                 plt.xlabel("Index")
#                 plt.ylabel(numerical_cols[0])
#                 plt.title(f"Bar Plot of {numerical_cols[0]}")
#             else:  # Line plot for larger datasets
#                 plt.plot(df.index, df[numerical_cols[0]], marker='o', color='skyblue')
#                 plt.xlabel("Index")
#                 plt.ylabel(numerical_cols[0])
#                 plt.title(f"Line Plot of {numerical_cols[0]}")

#             buffer = io.BytesIO()
#             plt.savefig(buffer, format='png')
#             buffer.seek(0)
#             image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
#             plt.close()
#             return image_base64, None
#         except Exception as e:
#             return None, f"Error generating visualization: {str(e)}"

#     @staticmethod
#     def process_query(query: str, visualize: bool) -> Tuple[Dict[str, Any], int]:
#         """Process a natural language query and return the result.

#         Args:
#             query: The natural language query string.
#             visualize: Whether to generate a visualization.

#         Returns:
#             Tuple of response dictionary and HTTP status code.
#         """
#         max_retries = 6
#         retry_delay = 5  # Increased delay for 1 QPS limit

#         for attempt in range(max_retries):
#             try:
#                 result = QueryModel.execute_query(query)
#                 break  # Success, exit retry loop
#             except Exception as e:
#                 error_str = str(e)
#                 if "rate_limit" in error_str:
#                     if attempt < max_retries - 1:
#                         print(f"Rate limit hit, retrying in {retry_delay} seconds... (Attempt {attempt + 1}/{max_retries})")
#                         time.sleep(retry_delay)
#                         continue
#                     else:
#                         return {"error": f"Max retries reached: {error_str}", "status_code": 429}, 429
#                 else:
#                     return {"error": f"Query failed: {error_str}", "status_code": 500}, 500

#         response = {"query": query, "result": result}

#         if visualize:
#             image_base64, error = QueryController.generate_visualization(result)
#             if image_base64:
#                 response["visualization"] = f"data:image/png;base64,{image_base64}"
#             elif error:
#                 response["visualization_error"] = error

#         time.sleep(1)  # Respect 1 QPS limit
#         return response, 200
from app.models.query_model import QueryModel
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
import time
from typing import Tuple, Dict, Any, Optional

class QueryController:
    @staticmethod
    def generate_visualization(data: Any) -> Tuple[Optional[str], Optional[str]]:
        """Generate a simple bar or line chart from numerical data.

        Args:
            data: Query result data (list, dict, or single value).

        Returns:
            Tuple containing base64-encoded image (or None) and error message (or None).
        """
        try:
            # Handle single-value results (e.g., counts)
            if isinstance(data, (int, float)):
                plt.figure(figsize=(4, 4))
                plt.bar([0], [data], color='skyblue')
                plt.xticks([0], ['Count'])
                plt.ylabel('Value')
                plt.title('Query Result')
                buffer = io.BytesIO()
                plt.savefig(buffer, format='png')
                buffer.seek(0)
                image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
                plt.close()
                return image_base64, None

            # Handle list or dict data
            df = pd.DataFrame(data)
            numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

            if len(numerical_cols) == 0:
                return None, "No numerical data available for visualization."

            plt.figure(figsize=(8, 6))
            if len(df) <= 10:  # Bar plot for small datasets
                plt.bar(df.index, df[numerical_cols[0]], color='skyblue')
                plt.xlabel("Index")
                plt.ylabel(numerical_cols[0])
                plt.title(f"Bar Plot of {numerical_cols[0]}")
            else:  # Line plot for larger datasets
                plt.plot(df.index, df[numerical_cols[0]], marker='o', color='skyblue')
                plt.xlabel("Index")
                plt.ylabel(numerical_cols[0])
                plt.title(f"Line Plot of {numerical_cols[0]}")

            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
            plt.close()
            return image_base64, None
        except Exception as e:
            return None, f"Error generating visualization: {str(e)}"

    @staticmethod
    def process_query(query: str, visualize: bool) -> Tuple[Dict[str, Any], int]:
        """Process a natural language query and return the result.

        Args:
            query: The natural language query string.
            visualize: Whether to generate a visualization.

        Returns:
            Tuple of response dictionary and HTTP status code.
        """
        max_retries = 6
        retry_delay = 5  # Increased delay for 1 QPS limit

        for attempt in range(max_retries):
            try:
                result = QueryModel.execute_query(query, visualize)  # Pass visualize flag
                break  # Success, exit retry loop
            except Exception as e:
                error_str = str(e)
                if "rate_limit" in error_str:
                    if attempt < max_retries - 1:
                        print(f"Rate limit hit, retrying in {retry_delay} seconds... (Attempt {attempt + 1}/{max_retries})")
                        time.sleep(retry_delay)
                        continue
                    else:
                        return {"error": f"Max retries reached: {error_str}", "status_code": 429}, 429
                else:
                    return {"error": f"Query failed: {error_str}", "status_code": 500}, 500

        response = {"query": query, "result": result}

        if visualize:
            image_base64, error = QueryController.generate_visualization(result)
            if image_base64:
                response["visualization"] = f"data:image/png;base64,{image_base64}"
            elif error:
                response["visualization_error"] = error

        time.sleep(1)  # Respect 1 QPS limit
        return response, 200