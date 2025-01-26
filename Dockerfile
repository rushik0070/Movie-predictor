FROM python
WORKDIR /app
COPY . /app
CMD ["python3","streamlit run app.py"]