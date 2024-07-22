from datetime import datetime
from sys import argv
from os.path import join
import subprocess


POST_DIR = r".\\_posts\\"


def safe_str(in_str: str) -> str:
    """
    Returns a Jekyll-safe version of the input string

        Parameters:
            in_str (str): Input string

        Returns:
            out_str (str): Jekyll-safe output string
    """
    out_str = in_str.lower()
    out_str = out_str.replace(" ", "-")
    return out_str


def main() -> None:
    front_matter = (
        "---\n"
        "layout: post\n"
        f"category: \"{modem_brand}\"\n"
        f"title: \"{modem_model}\"\n"
        f"date: \"{post_datetime}\"\n"
        "---"
    )
    post_template = """
<img src="{{ "assets/img/XXXXXX_front.jpg" | relative_url }}" class="modem_image">
<img src="{{ "assets/img/XXXXXX_rear.jpg" | relative_url }}" class="modem_image">

### Capabilities

| Service | Supported |
| :-: | :-: |
| ADSL | XXX |
| VDSL | XXX |
| FIBRE | XXX |
| VoIP | XXX |

### Login Information

| Provider | Username | Password | IP Address |
| :-: | :-: | :-: | :-: |
| Provider | Username | Password | IP_Address |

### Supporting Resources

| Resource | Link |
| :-: | :-: |
| Resource | [Link]() |
"""
    post_file_name = f"{post_date}-{safe_str(modem_brand)}-{safe_str(modem_model)}.md"
    post_file_path = join(POST_DIR, post_file_name)
    
    with open(post_file_path, "w") as outfile:
        outfile.writelines(front_matter + post_template)

    subprocess.run(["code", post_file_path])


if __name__ == "__main__":
    arg_size = len(argv) - 1
    
    if arg_size < 2:
        err_str = (
            f"2 arguments need be given, {arg_size} provided\n"
            "Your command should read \"./newpost.py 'modem brand' 'modem model'\"\n"
        )
        raise ValueError(err_str)
    
    modem_brand = argv[1]
    modem_model = argv[2]
    post_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    post_date = post_datetime[:10]

    main()
