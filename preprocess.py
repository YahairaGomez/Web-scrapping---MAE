import pandas as pd 
import os
import glob
from pathlib import Path
def reading_file(path):
    try:
        df = pd.read_excel(path, sheet_name="8. Max Potencia" )
        return df
    except FileNotFoundError:
        print(f"Error: el archivo {path} no existe.")
    except ValueError:
        print(f"Error: la hoja '8. Max Potencia' no existe en {path}.")
    except Exception as e:
        print(f"Error inesperado al leer {path}: {e}")
    
    return None

def get_id_by_name(df, columnWhereToLook, rowName):
    return df[df[columnWhereToLook] == rowName].index[0]


def preprocessing_one_file(df):
        
    ## Reducing the original df
    searched_column = 'Unnamed: 0'
    if searched_column not in df.columns:
        print("Columna 'Unnamed: 0' no encontrada, se omite archivo")
        return None

    # Buscar Total
    try:
        idx_total = get_id_by_name(df, searched_column, "Total")
    except IndexError:
        print("Fila 'Total' no encontrada, se omite archivo")
        return None
    
    df = df.loc[0:idx_total, 'Unnamed: 0':'Unnamed: 3']

    ## Changing the columns' name
    meses = df.iloc[5, 1:].apply(lambda x: pd.to_datetime(x).strftime('%b-%Y') if pd.notna(x) else x).tolist()
    columnas = ['Tipo de Generación'] + meses
    df.columns = columnas
    searched_column = "Tipo de Generación"
    
    ## Obtaining the Electric generation data (Last 3 months)
    try:
        idx_hidroelectrica = get_id_by_name(df, searched_column, "Hidroeléctrica")
    except IndexError:
        print("Fila 'Hidroeléctrica' no encontrada, se omite archivo")
        return None
    df = df.loc[idx_hidroelectrica:idx_total, :]


    ## Obtaining data from the current excel month
    latest_month = meses[-1]
    df_current_month = df[['Tipo de Generación', latest_month]].copy() 

    # Changing column's name
    df_current_month['Mes'] = pd.to_datetime(latest_month, format='%b-%Y').strftime('%b')
    df_current_month['Año'] = pd.to_datetime(latest_month, format='%b-%Y').strftime('%Y')
    df_current_month = df_current_month.rename(columns={latest_month: 'Consumo(MW)'})


    # Renaming values
    df_current_month = df_current_month.rename(columns={latest_month: 'Consumo(MW)'})

    return df_current_month

if __name__ == "__main__":
    df_list = []

    current_folder = Path.cwd()
   
    year_to_analyze_list = ["2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]
    for year_to_analyze in year_to_analyze_list:
        folder_path = current_folder / f"output_files/{year_to_analyze}"

        excel_files_path = glob.glob(str(folder_path / '*.xlsx'))

        if not excel_files_path:
            print(f"No hay archivos en {folder_path}")
        else:
            for file_path in excel_files_path:
                try:
                    df = reading_file(file_path)
                    df_current_month = preprocessing_one_file(df)
                    df_list.append(df_current_month)
                except Exception as e:
                    print(f"Skipping {file_path}: {e}")

    # Concatenar todos los DataFrames después de procesar todos los años
    if df_list:
        df_final = pd.concat(df_list, ignore_index=True)
        df_final.to_csv(current_folder / f"df_processed_final.csv", index=False)
    else:
        print("No se encontraron archivos válidos para procesar.")
    
