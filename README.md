# txt2xml

txt2xml is a python script for converting an Excel table to `strings.xml` file in Android. An Excel table is easy to manage the translations of strings while `strings.xml` is used by Android system to get the strings.

## How to use

Let's say we have an Excel table as bellow:

<table>
  <tr>
    <td></td>
    <td><b>zh</b></td>
    <td><b>fr</b></td>
    <td><b>es</b></td>
    <td><b>de</b></td>
  </tr>
  <tr>
    <td>Main.MenuShowHistory</td>
    <td>历史</td>
    <td>Historique</td>
    <td>Historial</td>
    <td>Verlauf</td>
  </tr>
  <tr>
    <td>Main.MenuShowDownloads</td>
    <td>下载</td>
    <td>Téléchargements</td>
    <td>Descargas</td>
    <td>Downloads</td>
  </tr>
  <tr>
    <td>Main.MenuPreferences</td>
    <td>配置</td>
    <td>Préférences</td>
    <td>Preferencias</td>
    <td>Einstellungen</td>
  </tr>
  <tr>
    <td>PreferencesActivity.EnableJavascriptPreferenceSummary</td>
    <td>如果不支持JavaScript，很多网站效果不能打开，建议打开.</td>
    <td>Active ou désactive le JavaScript.</td>
    <td>Activar o desactivar JavaScript.</td>
    <td>JavaScript ein-/ausschalten.</td>
  </tr>
</table>

> **Note:** The contents in first row of the table are language shortcode. The contents in first column of other rows are the name of strings in Android.

Save the table as a `Unicode text(*.txt)` file, for example, `strings.txt`.

**Run the script:**

```
python txt2xml.py strings.txt
```

Now, you will see it automatically created four new directories(`values-zh/`, `values-fr/`, `values-es/`, `values-de/`) with a separate `strings.xml` inside. 

The contents of `strings.xml` in `values-zh/`:

```
<?xml version="1.0" ?>
<resources>
  <string name="Main.MenuShowHistory">历史</string>
  <string name="Main.MenuShowDownloads">下载</string>
  <string name="Main.MenuPreferences">配置</string>
  <string name="PreferencesActivity.EnableJavascriptPreferenceSummary">如果不支持JavaScript，很多网站效果不能打开，建议打开.</string>
</resources>
```